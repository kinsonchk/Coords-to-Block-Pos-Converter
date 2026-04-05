To use the program, go to: https://www.onlineide.pro/playground/share/4cf82677-93f9-4465-b8bf-1be14d523054

Video tutorial and example walkthrough: https://www.youtube.com/watch?v=wq1AePig_z4

==========

Details:

The user needs to provide:
1.  The real-world coordinate boundaries (in latitude and longitude decimal degree format) of the area that you're trying to convert
2.  The grid's boundary positions (top-left and bottom-right block positions)
3.	A target position in real-world coordinates to convert

Using linear interpolation, the program calculates the equivalent block position by scaling longitude to the grid's x-axis and latitude (inverted north-to-south) to the grid's z-axis.

This tool helps ensure accurate mapping between real-world locations and virtual grids, making it useful for projects such as building real-world map replicas or visualizing GPS data in a block-based environment.
