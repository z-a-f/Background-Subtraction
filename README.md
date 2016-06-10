# Background-Subtraction

Background subtraction codes 


assign pixel_out =  ( {16{~blank_bg}} & pixel_temp ) |
                                ( {16{~blank_real}} & real_data ) |
                                ( {16{~blank_fg}} & {16{pixel_fg}});

pixel_temp={temp_bg[38:34],temp_bg[25:20],temp_bg[11:7]};    // background output pixel
temp_bg[39:27] =    proc_d[39:27]   - proc_d[39:34] + pixel_in[15:11];
temp_bg[26:13] =    proc_d[26:13]   - proc_d[26:20]     + pixel_in[10:5];
temp_bg[12:0] =     proc_d[12:0]    - proc_d[12:7]  + pixel_in[4:0];
proc_d = mem(temp_bg)

real_data = mem(temp_real)
temp_real = pixel_in

pixel_fg = mem(temp_fg)
temp_fg = (difference[15:11] > 15) | (difference[10:5] > 15) | (difference[4:0] > 15);
assign difference[15:11] = (temp_real[15:11] > pixel_temp[15:11]) ?
                                            (temp_real[15:11] - pixel_temp[15:11]) :
                                            (pixel_temp[15:11] - temp_real[15:11]);
assign difference[10:5] = (temp_real[10:5] > pixel_temp[10:5]) ?
                                            (temp_real[10:5] - pixel_temp[10:5]) :
                                            (pixel_temp[10:5] - temp_real[10:5]);
assign difference[4:0] = (temp_real[4:0] > pixel_temp[4:0]) ?
                                            (temp_real[4:0] - pixel_temp[4:0]) :
                                            (pixel_temp[4:0] - temp_real[4:0]);
