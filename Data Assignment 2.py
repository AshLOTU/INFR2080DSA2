#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pygame
import time

pygame.mixer.init()
swap_sound = pygame.mixer.Sound("swap_sound.wav")

step_counter = 1  

def mergesort(arr):
    global step_counter  

    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        mergesort(L)
        mergesort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            
            
            print(f"Step {step_counter}: {arr}")

        
            swap_sound.play()
            time.sleep(0.5)

            step_counter += 1  

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            
            
            print(f"Step {step_counter}: {arr}")

            step_counter += 1 

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            
            
            print(f"Step {step_counter}: {arr}")

            step_counter += 1 


arr_input = input("Enter numbers into array separated by spaces: ")
arr = [int(num) for num in arr_input.split()]
print(" ")
print("Initial Array:", arr)


mergesort(arr)
print(" ")
print("Sorted Array:", arr)

