python3 ../ex06/stres_test.py >> output1 & 
python3 ../ex06/stres_test.py > output2 & 
python3 ../ex06/stres_test.py &> std_out_err &
python3 ../ex06/stres_test.py 2> std_err_four >&1 &