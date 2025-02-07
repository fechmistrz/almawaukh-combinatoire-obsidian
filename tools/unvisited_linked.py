#!/usr/bin/env python3
import pywikibot as pw
import json
import sys
import logging



def clean_links(links):
    clean = list()
    bad_words = ["Draft", "Glossary of engineering", "Help", "MOS", "Portal", "Talk", "Template talk", "Template", "User talk", "Wikipedia talk", "Wikipedia"]
    dead_ends = ["Number density"]

    for link in links:
        is_bad = False
        for bad_word in bad_words:
            if f"{bad_word}:" in link:
                is_bad = True
                break
        if is_bad:
            continue
        clean.append(link)
    clean = [link for link in clean if link not in dead_ends]
    return sorted(list(set(clean)))


def get_links(page, direction="forward"):
    all_links = list()
    if direction == "forward":
        source = page.linkedPages()
    else:
        source = page.backlinks()

    for link in source:
        if type(link) == pw.page._page.Page:
            all_links.append(link.title())

    return clean_links(all_links)



def print_unvisited(final_database):
    import collections

    unvisited_links = list()
    for v in final_database.values():
        unvisited_links.extend(v["forward"])
        unvisited_links.extend(v["backward"])

    unvisited_links = collections.Counter([x for x in unvisited_links if x not in final_database.keys()])
    logging.info(f"Next pages to be visited: {', '.join([x[0] for x in unvisited_links.most_common(10)])}")

logging.basicConfig(encoding="utf-8", level=logging.INFO)

site = pw.Site("en", "wikipedia")
with open(sys.argv[1]) as f:
    database = json.load(f)


for k, v in database.items():
    forward = v.get("forward", [])
    backward = v.get("backward", [])
    if forward and backward:
        continue
    if v.get("dead", False):
        v["forward"] = list()
        v["backward"] = list()
        continue

    page = pw.Page(site, k)
    if not page.text:
        raise Exception(f"Page {k} does not exist at English Wikipedia!")

    if not forward:
        logging.info(f"Missing forward links in <{k}>")
        forward = get_links(page)
        logging.info(f"Found {len(forward)} links")
        v["forward"] = forward
    if not backward:
        logging.info(f"Missing backward links in <{k}>")
        backward = get_links(page, "backward")
        logging.info(f"Found {len(backward)} links")
        v["backward"] = backward

with open(sys.argv[1], "w") as f:
    database = {k: {
        "dead": v.get("dead", False),
        "forward": clean_links(v["forward"]),
        "backward": clean_links(v["backward"])}
    for k, v in database.items()}
    database = dict(sorted(database.items()))
    f.write(json.dumps(database, indent=2))

print_unvisited(database)