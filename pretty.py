import time

def solve(s):
    # 其实这种思路是可行的，但是效率太低了。

    # 使用 itertools 是个错误。。。或者说是使用的不对。
    # 回文子串，满足的条件是 第一个数与最后一个数是相等的。
    # 1. 找到所有的字串
    # 2. 查看字串的奇偶性，然后比较最长的字串
    # 3. 需要考虑 s == [], or [1]
    # 4. 下面就需要考虑一下效率了。。。时间限制


    s = list(s)
    want = []
    for start in range(len(s)):
        for end in range(start, len(s)):
            if start <= end:
                end += 1

                # 下面就是判断回文了。
                temp = s[start: end]        # 这个是 字串

                # 如果当前的回文字串已经大于下一个字串， 那么直接跳出来
                # 这里的写法上有点问题。逻辑是对的。
                # if len(want) > len(temp):
                #     break

                if len(temp) < len(want):
                    # print("differ here **********:  ", want, temp)
                    continue

                k = 1
                for m in range(len(temp) // 2 + 1):
                    if temp[m] != temp[-m - 1]:
                        k *= 0      # 此时第一次首位相等
                        break
                    else:
                        k *= 1     # 否则的话，就直接 排除掉了。

                # print(k)
                if k != 0:
                    # print(temp)
                    if len(want) < len(temp):
                        want = temp


        start += 1

    print("this is the final res: ", want)
    return ''.join(want)

# s = 'a'
# 为什么无法通过这个测试用例呢 ？？？
# s = "aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa"
s = "gphyvqruxjmwhonjjrgumxjhfyupajxbjgthzdvrdqmdouuukeaxhjumkmmhdglqrrohydrmbvtuwstgkobyzjjtdtjroqpyusfsbjlusekghtfbdctvgmqzeybnwzlhdnhwzptgkzmujfldoiejmvxnorvbiubfflygrkedyirienybosqzrkbpcfidvkkafftgzwrcitqizelhfsruwmtrgaocjcyxdkovtdennrkmxwpdsxpxuarhgusizmwakrmhdwcgvfljhzcskclgrvvbrkesojyhofwqiwhiupujmkcvlywjtmbncurxxmpdskupyvvweuhbsnanzfioirecfxvmgcpwrpmbhmkdtckhvbxnsbcifhqwjjczfokovpqyjmbywtpaqcfjowxnmtirdsfeujyogbzjnjcmqyzciwjqxxgrxblvqbutqittroqadqlsdzihngpfpjovbkpeveidjpfjktavvwurqrgqdomiibfgqxwybcyovysydxyyymmiuwovnevzsjisdwgkcbsookbarezbhnwyqthcvzyodbcwjptvigcphawzxouixhbpezzirbhvomqhxkfdbokblqmrhhioyqubpyqhjrnwhjxsrodtblqxkhezubprqftrqcyrzwywqrgockioqdmzuqjkpmsyohtlcnesbgzqhkalwixfcgyeqdzhnnlzawrdgskurcxfbekbspupbduxqxjeczpmdvssikbivjhinaopbabrmvscthvoqqbkgekcgyrelxkwoawpbrcbszelnxlyikbulgmlwyffurimlfxurjsbzgddxbgqpcdsuutfiivjbyqzhprdqhahpgenjkbiukurvdwapuewrbehczrtswubthodv"

# s = 'caabbbd'
# s = 'babad'

t1 = time.time()
solve(s)
t2 = time.time()

print(t2 - t1)       # 5.91, 0.46

# 2.266845226287842
"""
 # 这里需要判断 center 是不是一个回文字串
            k = 1
            for m in range(len(center) // 2 + 1):
                if center[m] != center[-m - 1]:
                    k *= 0  # 此时第一次首位相等
                    break
                else:
                    k *= 1  # 否则的话，就直接 排除掉了。
            if k != 0:
                if len(want) <= len(center):
                    want = center
                    print("ooooh, find one ************* :", want)
            # 到这里已经是找到了一个字串

 # k = 1
            # for m in range(len(even) // 2 + 1):
            #     if even[m] == even[-m-1]:
            #         k *= 1
            #     else:
            #         k *= 0
            #     if k != 0 and len(want) <= len(even):       # 测试的话，就写为 <=
            #         want = even
            #         print("find one! **********: ", want)
            #
            
            
# 原本的算法如果改变一下 回文检查那一部分再测试的话，估计会快些的。



        # 2. 以 2 为中心往2侧拓展, 开始的长度是. 假设已经是偶数了。那么怎么移动呢？
        # 此时的 even 也只是一个字串而已
        # 偶数这部分是可行的了
        # 这部分整体就是按照一个假设开始的，那就是 偶数个字串。。。
        # step = 0
        # while step < len(s) // 2+1:
        #     if start - step < 0:
        #         even = s[0: start + 2 + step]
        #     else:
        #         even = s[start - step: start + step + 2]
        #
        #     if len(even) < len(want):
        #         break
        #     else:
        #         print(step, even, "aaaaa")
        #         if len(even) % 2 == 0:  # 确保都是偶数。。。
        #             # 用另一种写法来判断是否为回文
        #             t = len(even) // 2
        #             if even[:t] == list(reversed(even[t:])) and len(want) <= len(even):
        #                 want = even
        #                 print("find one! **********: ", even)
        #                 print(start, step, start-step+2)    # tt 4--6
        #                 step += 1
        #             else:
        #                 break
        #         else:
        #             break


 for i in range(len(s)):

        s1 = s[i: i+1]
        print(s1)

        s2 = s[i: i+2]
        print(s2)
        
        
        
 # 根本问题上还是出现在，到底如何判断一个 子串 是一个回文子串。。。
    # 总体上分为2中情况，即起始处的 奇偶：
    for i in range(len(s)):

        s1 = s[i: i+1]
        if len(s1) % 2 == 1:
            print(s1)
            left1 = i
            right1 = i

            while left1 >= 0 and right1 <= len(s1) and s1[left1] == s1[right1]:
                print("find one! **********: ", s1)
                left1 -= 1
                right1 += 1

        s2 = s[i: i + 2]
        if len(s2) % 2 == 0:
            print(s2)
            left2 = i
            right2 = i+1
            while left2 >= 0 and right2 <= len(s2) and s2[left2] == s2[right2]:
                print("find one! **********: ", s2)
                left2 -= 1
                right2 += 1

"""
