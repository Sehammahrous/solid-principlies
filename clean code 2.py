def calculate_result(a:int ,b:int,c:int)-> int:
    
    """
    find result dependent on the input whether even or odd
    Parameters:
    a (int): الحد الأقصى للعدد الذي يتم تكراره (أقل من هذا العدد).
    b (int): العامل الذي يتم ضربه في الأعداد الزوجية.
    c (int): العامل الذي يتم ضربه في الأعداد الفردية.

    Returns:
    int: النتيجة النهائية بعد جمع القيم المقررة لكل عدد
    """

    result=0
    for i in range(a):
        if i % 2 ==0:
            result += i*b
        else:
            result += i*b
    return result 
            