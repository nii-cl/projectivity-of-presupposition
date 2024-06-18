import pandas as pd
import random

np_human_list = [
    "teacher", "dancer", "doctor", "child", "boy", "girl", "student", "athlete", "kid",
    "professor", "singer", "director", "manager", "worker", "assistant", "stranger", "man", "woman"
]

name_list = [
    "John", "Tom", "Mary", "Bob", "Steven", "Jack", "Jim", "Katy", "Jason", "Ben", "Kyle", "Jenny"
]

v_dic = {
    "bet $100 on the race": "betting $100 on the race",
    "burst into the room": "bursting into the room",
    "cast bronze into a statue": "casting bronze into a statue",
    "hit the ball with the bat": "hitting the ball with the bat",
    "hurt others": "hurting others",
    "let the blinds down": "letting the blinds down",
    "put the book on the shelf": "putting the book on the shelf",
    "read the letter": "reading the letter",
    "set the dish on the table": "setting the dish on the table",
    "shed tears": "shedding tears",
    "shut the door": "shutting the door",
    "slit the envelope": "slitting the envelope",
    "split the log": "splitting the log",
    "spread the rumor": "spreading the rumor",
    "thrust the fork into the cake": "thrusting the fork into the cake",
    "upset the boat": "upsetting the boat"
}

modal_list = ["would", "could"]

Tr_dic = {
    "meet": "met", "see": "saw", "respect": "respected", "kick": "kicked", "love": "loved", "beat": "beat",
    "avoid": "avoided", "chase": "chased", "comfort": "comforted", "deceive": "deceived", "find": "found"
}

TrPP_list = [
    "met", "seen", "respected", "kicked", "loved", "beaten", "avoided", "chased", "comforted", "deceived", "found"
]

CSV_dic = {
    "quit": "quit", "gave up": "give up", "stopped": "stop", "continued": "continue", "kept": "keep",
    "ceased": "cease", "finished": "finish"
}

Factive_dic = {
    "regretted": "regret", "remembered": "remember", "forgot": "forget"
}

MAdv_list = [
    "quickly", "quietly", "happily", "angrily", "slowly", "sadly", "anxiously", "easily", "calmly"
]

TAdv_list = ["before", "after", "while", "when"]

aux_list = ["should", "could", "can", "must",
            "might", "may", "has to", "would"]

Comparative_list = ["better", "earlier", "more seriously", "worse"]


def develop(ws, ps, hs, label, htag, arg, stag, pairs, rate):
    allset = range(rate)
    testsplit = random.sample(allset, 5)

    replacements = {
        "VP1": random.choice(list(v_dic.keys())),
        "VP2": random.choice(list(v_dic.keys())),
        "VP3": random.choice(list(v_dic.keys())),
        "Tr": random.choice(list(Tr_dic.keys())),
        "Pst": Tr_dic.get(random.choice(list(Tr_dic.keys()))),
        "Ving": random.choice(list(v_dic.values())),
        "VPing": random.choice(list(v_dic.values())),
        "NP1": random.choice(np_human_list),
        "NP2": random.choice(np_human_list),
        "NP3": random.choice(np_human_list),
        "CSV": random.choice(list(CSV_dic.keys())),
        "Pre": CSV_dic.get(random.choice(list(CSV_dic.keys()))),
        "modal": random.choice(modal_list),
        "MAdv": random.choice(MAdv_list),
        "TAdv": random.choice(TAdv_list),
        "TrPP": random.choice(TrPP_list),
        "Comparative": random.choice(Comparative_list),
        "Factive": random.choice(list(Factive_dic.keys())),
        "FP": Factive_dic.get(random.choice(list(Factive_dic.keys()))),
        "Name": random.choice(name_list),
        "Aux": random.choice(aux_list),
        "comma": ',',
        "period": '.'
    }

    for i in allset:
        pss, hss = ps, hs

        for key, val in replacements.items():
            if key in ws:
                pss = pss.replace(key, val)
                hss = hss.replace(key, val)

        split = "test" if i in testsplit else "train"
        pairs.append([pss.strip(), hss.strip(), label, htag, arg, stag, split])

    return pairs


def main():
    pairs = []
    with open("template/TEMPLATE_FILE_NAME.csv") as f:
        finput = f.readlines()

    for line in finput:
        ps, hs, label, htag, arg, stags = line.strip().split(",")[0:6]
        if ps == "sentence1":
            continue

        ws = ps.split(" ") + hs.split(" ")
        stag = stags.split(';')[0]
        pairs = develop(ws, ps, hs, label, htag, arg, stag, pairs, 1)

    df = pd.DataFrame(pairs, columns=[
                      "sentence1", "sentence2", "label", "heuristics", "example1", "example2", "split"])
    df.to_csv("data/RESULTING_DATASET_NAME.tsv", sep="\t", index=True)


if __name__ == '__main__':
    main()
