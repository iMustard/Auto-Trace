import random
import sys
FAILED_SIGN = 'EvenNum'
PASS_SIGN = 'OddNum'


def auto_trace(input_list):

    if len(input_list) == 2: # no version between current day's failed version and previous day's pass version, just recheck.
        previous_version_status = determine_odd_even(input_list[0])
        if previous_version_status == FAILED_SIGN:
            print('Start Version also failed!')
            return -1
        else:
            current_version_status = determine_odd_even(input_list[1])
            if current_version_status == FAILED_SIGN:
                return input_list
            else:
                print('End Version also PASS!')
                return -1
    
    elif len(input_list) > 2: #when trace versions are more than 2, do this. Include current day's failed version and previous day's pass version.
        middle_version_num = int(len(input_list)/2) # Take the middle version's num in list.
        cur_trace_version = input_list[middle_version_num] # Current version (middle version) which will to be traced
        middle_version_status = determine_odd_even(cur_trace_version) # Run and get middle version's result.
        if middle_version_status == FAILED_SIGN:                             
            previous_version_status = determine_odd_even(input_list[0])   # Run and get previous day's version's result.
            if previous_version_status == FAILED_SIGN:
                print('Start Version also failed!') # Previous day's version rerun failed. 
                return -1
            else:   
                temp_list_raw = input_list[0:middle_version_num+1] # gen the new list to trace. list[0] == PASS, list[-1] == FAILED
                   
        else:
            current_version_status = determine_odd_even(input_list[-1])
            if current_version_status == FAILED_SIGN:
                temp_list_raw = input_list[middle_version_num:] # gen the new list to trace. list[0] == PASS, list[-1] == FAILED
            else:
                print('End Version also PASS!') # current day's  version rerun pass.
                return -1
    else:
        sys.exit(-1)

    print('temp_list_raw:', temp_list_raw)
    while len(temp_list_raw) > 2:  
        temp_medium = int(len(temp_list_raw)/2) # Bisection method.
        if determine_odd_even(temp_list_raw[temp_medium]) == FAILED_SIGN:
            temp_list_raw = temp_list_raw[0:temp_medium+1]  # list[0] == PASS, list[-1] == FAILED
        else:
            temp_list_raw = temp_list_raw[temp_medium:] # list[0] == PASS, list[-1] == FAILED
    
    
    if len(temp_list_raw) == 2:  # list[0] == PASS, list[-1] == FAILED
        #failed_version = temp_list_raw[1]
        #pass_version = temp_list_raw[0]
        return temp_list_raw


def determine_odd_even(input_num):
    '''judge'''
    print('aaa')
    print(input_num)
    if (int(input_num) % 2) == 0:
        judge_num = 'EvenNum'
    else:
        judge_num = 'OddNum'
    return judge_num

def determine_odd_even_2(input_num):
    if (int(input_num) % 2) == 0:
        judge_num = 'EvenNum'
    else:
        judge_num = 'OddNum'
    return judge_num

def gen_list_random():
    '''Gen a list used to test.'''
    list_a = []
    list_b = []
    while True:
        temp_num = random.randint(1,100000)
        temp_num_judge = determine_odd_even_2(temp_num)
        if temp_num_judge == FAILED_SIGN and temp_num not in list_b:
            list_b.append(temp_num)
        else:
            if temp_num not in list_a:
                list_a.append(temp_num)
        if len(list_a) > 50 and len(list_b) > 50:
            break
    aa = random.randint(0,5)
    bb = random.randint(0,5)
    list_a_end  = list_a[0:aa]
    list_b_end  = list_b[0:bb]
    list_end = list_a_end + list_b_end
    return list_end


if __name__ == '__main__':
    '''The main func.'''

    input_list = [1,3,5,7,10]
    input_list = gen_list_random()
    print('input_list:', input_list)
    print('listlenth is: ', len(input_list))
    trace_failed_version = auto_trace(input_list)
    if trace_failed_version == -1:
        sys.exit(-1)
    else:
        pass_version = trace_failed_version[0]
        failed_version = trace_failed_version[1]
        print('pass_version is', pass_version)
        print('failed_version is ', failed_version)
