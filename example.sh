clear
#for i in $(seq -f "%01g" 1 1 48)
#do
#	cp /home/climdes1/WRF/ARWpost/t2m"$i".jpg /home/climdes1/WRF/ARWpost/github2/
#done
git init
git add .
git commit -m "w"
git remote rm origin
git remote add origin https://github.com/JulioMtzSan/wrf.git
#git push --set-upstream origin master
git push -f -u origin main
