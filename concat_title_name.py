import argparse

def concat_job_title_and_name(namedir, titledir, outdir, max_length_ratio=None):
    """
    Concat job title and name and save output to file
    """
    with open(outdir, mode='w', encoding='utf-8') as out_file:
        out_file.seek(0)
        with open(titledir, encoding='utf-8') as title_file:
            for title in title_file:
                title = title.strip()
                if len(title) == 0: continue
                with open(namedir, encoding='utf-8') as name_file:
                    for name in name_file:
                        name = name.strip()
                        if len(name) == 0: continue
                        if max_length_ratio and len(title)/len(name) > max_length_ratio: continue     
                        out_file.write(f"{title} | {name}\n")
        out_file.truncate()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate name stamp images from text")
    parser.add_argument('-n', '--namedir', type=str, default="name.txt", required=False, 
                        help="Directory to file containing name") 
    parser.add_argument('-t', '--titledir', type=str, default="title.txt", required=False, 
                        help="Directory to file containing job title")
    parser.add_argument('-o', '--outdir', type=str, default="title_name.txt", required=False, 
                        help="Path to file for saving output")
    parser.add_argument('-lr', '--max_length_ratio', type=float, default=None, required=False, 
                        help="The maximum length ratio of job title over name, only concat pair with smaller ratio than that")
    args = parser.parse_args()

    concat_job_title_and_name(namedir=args.namedir, 
                              titledir=args.titledir, 
                              outdir=args.outdir,
                              max_length_ratio=args.max_length_ratio)