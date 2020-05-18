humanseg = hub.Module( name="deeplabv3p_xception65_humanseg" )
result = humanseg.segmentation( data={"image": [tmp_png_file_name]} )