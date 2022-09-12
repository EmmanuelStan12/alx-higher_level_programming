#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            one = my_list_1[i]
            two = my_list_2[i]
            result = one / two
            new_list.append(result)
        except ValueError:
            new_list.append(0)
        except TypeError:
            new_list.append(0)
            print("wrong type")
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except IndexError:
            new_list.append(0)
            print("out of range")
        finally:
            continue
    return new_list
