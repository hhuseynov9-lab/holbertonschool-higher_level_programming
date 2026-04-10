#!/usr/bin/python3
def best_score(a_dictionary):
    # Əgər lüğət boşdursa və ya None-dırsa
    if not a_dictionary:
        return None
    
    # Ən yüksək balı tapırıq
    max_val = max(a_dictionary.values())
    
    # Həmin bala uyğun olan İLK açarı qaytarırıq
    for i in a_dictionary:
        if a_dictionary[i] == max_val:
            return i  # Tapdıq və dərhal funksiyanı bitirib nəticəni qaytarırıq
