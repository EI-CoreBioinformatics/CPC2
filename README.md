* 2017-03-6 21:00, Yu-jian Kang

Here is a temporary package of CPC2. This package has been completely ported to Python3 and necessitates the C/C++
toolchain for being installed properly.

1) Pre-requisite:

a. Biopython package: a local version could be downloaded from
http://biopython.org/wiki/Download

b. GCC toolchain. On e.g. Ubuntu, do
sudo apt install build-essential

2) Install

python setup.py bdist_wheel && pip install dist/*whl

will suffice.

3) Run the predict

$ CPC2 -i (input_seq) -o (result_in_table)

example:
$ CPC2 -i data/example.fa -o example_output

4) Output result

Result in table format (delimited by tab):
#ID	peptide_length	Fickett_score	isoelectric_point	ORF_integrity	coding_probability	coding_label


	See the website for tutorial and more details. (http://cpc2.cbi.pku.edu.cn)

	This is a beta version of CPC2, if have any questions please report to us.

	Contact: cpc@mail.cbi.pku.edu.cn
