touch icecream.log
echo "--- post problem scripts ---" >> icecream.log
echo -e "\t$PWD" >> icecream.log

cp main.py main.md
python /data/configs/post_problem_scripts/ipynb_download_problem.py
