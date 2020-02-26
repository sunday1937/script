#!/usr/bin/env bash
selected=sh600352,sh600667,sh600745,sh600584,sz300346,sh600703,sz002157,sz000401,sz002074,sh603799,sz300623,sz002594,sz002180,sh512480,sh515700,sh000001,sz399006
currTime=$(date +%s)

# get result
curlResult=$(curl http://sqt.gtimg.cn/utf8/q\=${selected}\&_t\=${currTime})
# result=$(pwd)
# echo "result:${curlResult}"

# del " in curlResult
# curlResult=$(${curlResult} | sed ‘s/=//g’)
# echo "result:${curlResult}"

resultArray=(${curlResult//;/})

# echo ${resultArray[@]}

# echo "count:${#resultArray[@]}"


RESTORE=$(echo '\033[0m')
RED=$(echo '\033[00;31m')
GREEN=$(echo '\033[00;32m')
YELLOW=$(echo '\033[00;33m')
BLUE=$(echo '\033[00;34m')
MAGENTA=$(echo '\033[00;35m')
PURPLE=$(echo '\033[00;35m')
CYAN=$(echo '\033[00;36m')
LIGHTGRAY=$(echo '\033[00;37m')
LRED=$(echo '\033[01;31m')
LGREEN=$(echo '\033[01;32m')
LYELLOW=$(echo '\033[01;33m')
LBLUE=$(echo '\033[01;34m')
LMAGENTA=$(echo '\033[01;35m')
LPURPLE=$(echo '\033[01;35m')
LCYAN=$(echo '\033[01;36m')
WHITE=$(echo '\033[01;37m')


# 循环遍历
for item in ${resultArray[@]}
do
	# echo ""
	# echo "1. item:$item"
	# echo "2. -----------------------"
	matchResult=$(echo $item | grep "v_")
	# echo "matchResult:$matchResult"
	if [[ "${matchResult}" != "" ]]
	then
		# echo "3. --------- true"
		itemArray=(${item//\"/})
		# echo "itemArray[0]:${itemArray[0]}"
		# echo "itemArray[1]:${itemArray[1]}"
		realString=${itemArray[0]}
		# echo "realString:${realString}"


		# realArray=(${realString//\~/})
		realArray=(${realString//\~/ })  

		belleName=${realArray[1]}
		belleOpenPrice=${realArray[4]}
		belleCurrPrice=${realArray[3]}
		# belleIncrease=`expr $belleCurrPrice - $belleOpenPrice`
		# echo $belleIncrease

		belleIncrease=$(echo "$belleCurrPrice - $belleOpenPrice"|bc)
		# echo $belleIncrease

		# echo "scale=2;5 / 2"|bc
		bellePercent=$(echo "scale=3;$belleIncrease / $belleOpenPrice"|bc)
		# echo "bellePercent:$bellePercent"

		bellePercentFormat=$(echo "scale=2;$bellePercent * 100.0"|bc)
		# echo "bellePercentFormat:$bellePercentFormat"
		# echo "${bellePercentFormat:0:3}%"

		isGood=$(echo "$belleCurrPrice > $belleOpenPrice"|bc)
		# echo "isGood:${isGood}"
		if [[ $isGood == 1 ]]; then
			echo "${LRED}${belleName:0:2} ${bellePercentFormat:0:4}% ${belleOpenPrice} ${belleCurrPrice}"
		else
			echo "${BLUE}${belleName:0:2} ${bellePercentFormat:0:5}% ${belleOpenPrice} ${belleCurrPrice}"
		fi
		# echo "${RED}${belleName:0:1} ${bellePercentFormat:0:3}% ${belleOpenPrice} ${belleCurrPrice}"
		# echo ''
		# echo "${realArray[1]} ${realArray[4]} ${realArray[3]}"
		# for realItem in ${realArray[@]}
		# do
		# 	echo "${realItem}"
		# done


		# echo "4. itemArray:${itemArray[@]}"
		# echo "count:${#itemArray[*]}"
	fi
done
