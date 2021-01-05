# Youtube Playlist

## Prerequisite

- Create OAuth Credentials of type **Desktop App** 
## Multi-sheet

> Each sheet for each playlist. But this is cumbersome, so we have added same sheet all videos from all playlists.

### Check number of sheets in Excel (Cross-verifiy)

[Link](https://quadexcel.com/wp/formula-to-count-the-number-of-sheets-in-the-excel/)

1. Click ‘Ctrl+F3’, then ‘Name Manager’ Box Appears
2. Click ‘New’ (use shortcut key Alt+N)
3. Then, ‘New name’ box appears
4. Enter ‘Name’ as “CountSheets“(Your choice)
5. Enter ‘Refer To’ as =GET.WORKBOOK(1)&T(NOW())
6. Click OK
7. It takes you to the ‘Name Manager’ box again (you can find the Defined Name in the list)
8. Click ‘Close’

9. Come to the Cell, where you want to enter the Formula
10. Enter the Formula as =COUNTA(INDEX(CountSheets,0))
11. Click Enter


## Single Sheet

> Single sheet. 

NOTE:

- Delete all entries in `Test_SingleSheet.xlsx` but not the file to make it work.
- **TODO**: Add last updated timestamp to get most recent videos
- **TODO**: Add JSON to get `channelId` and Excel File name as input