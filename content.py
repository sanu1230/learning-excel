"""
Course content for the plain teaching app - no login, no storage, no file
exchange. Each chapter has three parts:
  notes    - theory, shown as bullet points
  practice - a numbered list of things to actually try in Excel on the
             learner's own computer, self-directed, never checked
  quiz     - multiple choice, 2 attempts per question, then the correct
             answer is revealed. Doesn't gate anything - "Done" always works.

Chapter dict shape:
{
  "id": "U1C1",
  "num": 1,
  "title": "...",
  "notes": ["bullet", ...],
  "practice": ["step 1", "step 2", ...],
  "quiz": [{"q": "...", "options": [...], "answer": 0}, ...],
}
"""

UNIT1_CHAPTERS = [
    dict(
        id="U1C1",
        num=1,
        title="What is Excel & What It's Used For",
        notes=[
            "Excel is a spreadsheet program: it stores information in a grid of rows and columns.",
            "Each small box in the grid is called a cell. A cell is named by its column letter and row number, e.g. B3.",
            "People use Excel to organize lists, do calculations automatically, track money, analyze data, and build charts.",
            "Real examples: a class marksheet, a monthly pocket-money tracker, a cricket team's scorecard, a school attendance register.",
            "The real power of Excel: change one number, and every total or chart connected to it updates by itself. Paper and plain text lists cannot do that.",
            "A single Excel file is called a workbook. A workbook can hold many worksheets (tabs) inside it.",
        ],
        practice=[
            "Open Excel and start a new blank workbook.",
            "In column B, type the names of 3 friends or classmates, one per row (B2, B3, B4).",
            "In column C, type a favorite subject for each. In column D, type a mark out of 100.",
            "Click on a few different cells and watch the Name Box (top-left) show you exactly which cell you're in, e.g. C3.",
            "Change one of the marks in column D. Notice nothing else updates yet - that's expected. You'll connect cells with formulas from Chapter 3 onward.",
        ],
        quiz=[
            dict(q="What do we call the small box where a row and a column meet?", options=["Cell", "Range", "Field", "Tab"], answer=0),
            dict(q="True or False: in Excel, changing one number can update related totals automatically (once formulas are involved).", options=["True", "False"], answer=0),
            dict(q="What do we call an Excel file that can hold many worksheets inside it?", options=["Workbook", "Worksheet", "Document", "Folder"], answer=0),
            dict(q="If you type a value into cell C3, what does the Name Box show while that cell is selected?", options=["C3", "Cell 3", "Row C", "3C"], answer=0),
        ],
    ),
    dict(
        id="U1C2",
        num=2,
        title="Interface Tour: Ribbon, Tabs, Quick Access Toolbar",
        notes=[
            "The Ribbon is the strip of buttons and icons across the top of Excel, organized into tabs.",
            "Common tabs: Home (formatting, fonts), Insert (charts, tables), Formulas (functions), Data (sorting, filtering), View (freeze panes, zoom).",
            "The Quick Access Toolbar sits above or below the Ribbon and holds shortcuts you use constantly, like Save and Undo.",
            "The Formula Bar (below the Ribbon) shows exactly what is typed in the selected cell, including formulas.",
            "The Name Box (left of the Formula Bar) shows which cell is currently selected, and lets you jump straight to a cell by typing its reference.",
            "The Status Bar at the bottom shows quick info like the sum or average of any cells you've selected.",
        ],
        practice=[
            "Open Excel (or switch to the workbook from Chapter 1).",
            "Find and point to: the Ribbon, the Formula Bar, the Name Box, the Status Bar.",
            "Click through the Home, Insert, and Formulas tabs on the Ribbon and notice the buttons change.",
            "Select a couple of number cells and look at the Status Bar - it shows their Sum and Average automatically.",
            "Type a cell reference like D10 into the Name Box and press Enter - it jumps straight there.",
        ],
        quiz=[
            dict(q="Which part of Excel shows exactly what you typed into the selected cell?", options=["Formula Bar", "Status Bar", "Name Box", "Ribbon"], answer=0),
            dict(q="Which tab would you open to insert a chart?", options=["Insert", "Home", "Data", "View"], answer=0),
            dict(q="Which part lets you type a cell reference to jump straight to it?", options=["Name Box", "Formula Bar", "Ribbon", "Status Bar"], answer=0),
            dict(q="Which bar at the bottom shows a quick sum of selected cells?", options=["Status Bar", "Formula Bar", "Ribbon", "Title Bar"], answer=0),
        ],
    ),
    dict(
        id="U1C3",
        num=3,
        title="Workbooks, Worksheets & File Structure",
        notes=[
            "A workbook is the entire Excel file (it ends in .xlsx). A worksheet is one tab inside that file.",
            "A new workbook opens with one worksheet by default, but you can add as many as you need.",
            "Worksheet tabs sit at the bottom of the window - click a tab to switch sheets, right-click for options like Rename, Delete, or Move.",
            "Sheets in one workbook can reference each other, e.g. a Summary sheet can pull totals from a Sales sheet.",
            "Saving: Ctrl+S saves the workbook. The default modern format is .xlsx; older files may be .xls; data-only exports often use .csv.",
        ],
        practice=[
            "In your workbook, click the + button next to the sheet tabs to add a new sheet.",
            "Right-click the new tab and choose Rename - call it 'Practice'.",
            "Right-click again and try Move or Copy to reorder your tabs.",
            "Press Ctrl+S to save. Notice the file extension Excel saves as by default.",
        ],
        quiz=[
            dict(q="What do we call the entire Excel file, which can contain many sheets?", options=["Workbook", "Worksheet", "Cell", "Range"], answer=0),
            dict(q="What do we call a single tab inside a workbook?", options=["Worksheet", "Workbook", "Window", "Panel"], answer=0),
            dict(q="What is the modern default file extension for an Excel workbook?", options=[".xlsx", ".xls", ".csv", ".doc"], answer=0),
            dict(q="Right-clicking a sheet tab lets you Rename, Delete, or do what else?", options=["Move", "Print", "Merge", "Sort"], answer=0),
        ],
    ),
    dict(
        id="U1C4",
        num=4,
        title="Navigating Cells, Rows, Columns & Ranges",
        notes=[
            "Every cell has an address: column letter first, then row number - e.g. C5 means column C, row 5.",
            "A range is a group of cells, written as start:end - e.g. B2:B6 means cells B2, B3, B4, B5, B6.",
            "Arrow keys move one cell at a time. Ctrl+Arrow jumps to the edge of a block of data.",
            "Ctrl+Home jumps to cell A1. Ctrl+End jumps to the last used cell in the sheet.",
            "Click a cell and drag to select a range, or click a column/row header to select the whole column/row.",
        ],
        practice=[
            "In your workbook, click cell A1, then press Ctrl+End - see where it jumps.",
            "Press Ctrl+Home to come back to A1.",
            "Click cell B2 and drag down to B6 to select the range B2:B6.",
            "Click a column header (like the letter C at the top) to select the whole column.",
        ],
        quiz=[
            dict(q="What is the cell reference for row 5, column C?", options=["C5", "5C", "R5C3", "C-5"], answer=0),
            dict(q="How many cells are in the range B2:B6?", options=["5", "4", "6", "3"], answer=0),
            dict(q="Which keyboard shortcut jumps straight to cell A1?", options=["Ctrl+Home", "Ctrl+End", "Ctrl+Arrow", "Ctrl+Tab"], answer=0),
            dict(q="Which key combination jumps to the edge of a block of data?", options=["Ctrl+Arrow", "Ctrl+Shift+Arrow", "Ctrl+Home", "Alt+Arrow"], answer=0),
        ],
    ),
    dict(
        id="U1C5",
        num=5,
        title="Entering & Editing Data",
        notes=[
            "Click a cell and start typing to enter data. Press Enter to confirm and move down, or Tab to confirm and move right.",
            "Press F2 (or double-click a cell) to edit its existing content instead of replacing it.",
            "Press Esc to cancel an edit before confirming it.",
            "AutoComplete: if a column already has text like 'Mumbai', typing 'Mu' again will suggest it - press Enter to accept or keep typing to override.",
            "Numbers align right by default, text aligns left - a quick visual check that Excel read your entry as the type you intended.",
        ],
        practice=[
            "Type a value into a blank cell and press Tab instead of Enter - notice which direction the cursor moves.",
            "Press F2 on a cell that already has text in it, and edit it without retyping the whole thing.",
            "Start editing a cell, then press Esc - confirm your original value is unchanged.",
            "Type the same city name into two cells in the same column and watch AutoComplete suggest it the second time.",
        ],
        quiz=[
            dict(q="Which key lets you edit a cell's existing content instead of replacing it?", options=["F2", "F1", "Esc", "Tab"], answer=0),
            dict(q="Which key cancels an edit before you confirm it?", options=["Esc", "F2", "Delete", "Backspace"], answer=0),
            dict(q="Pressing Tab after typing a value moves the cursor which direction?", options=["Right", "Down", "Left", "Up"], answer=0),
            dict(q="By default, do numbers align left or right in a cell?", options=["Right", "Left", "Center", "Justified"], answer=0),
        ],
    ),
    dict(
        id="U1C6",
        num=6,
        title="Copy, Cut, Paste & Paste Special",
        notes=[
            "Ctrl+C copies a cell or range (keeps the original in place). Ctrl+X cuts it (removes the original once pasted).",
            "Ctrl+V pastes everything: value, formula, and formatting.",
            "Paste Special (Ctrl+Alt+V) lets you paste only what you want - e.g. Values Only (no formulas), or Formats Only (no data).",
            "Values Only paste is very common: it 'freezes' a formula's result as a plain number.",
            "Dragging the small square at a cell's bottom-right corner (the Fill Handle) copies a value or pattern into neighboring cells.",
        ],
        practice=[
            "Copy a cell with Ctrl+C, click a different cell, and paste it with Ctrl+V.",
            "Try Ctrl+X on a different cell, then paste it elsewhere - notice the original disappears.",
            "Copy a cell, then use Ctrl+Alt+V (Paste Special) and choose Values Only somewhere else.",
            "Type a value, then drag the small square at the cell's bottom-right corner (the Fill Handle) down a few rows.",
        ],
        quiz=[
            dict(q="Which shortcut copies a cell while keeping the original in place?", options=["Ctrl+C", "Ctrl+X", "Ctrl+V", "Ctrl+Z"], answer=0),
            dict(q="Which shortcut removes the original once pasted elsewhere?", options=["Ctrl+X", "Ctrl+C", "Ctrl+V", "Ctrl+D"], answer=0),
            dict(q="Which Paste Special option 'freezes' a formula's result as a plain number?", options=["Values Only", "Formats Only", "Formulas Only", "All"], answer=0),
            dict(q="What is the small square at a cell's bottom-right corner called?", options=["Fill Handle", "Selection Box", "Anchor Point", "Grip"], answer=0),
        ],
    ),
    dict(
        id="U1C7",
        num=7,
        title="Undo/Redo, AutoSave & File Formats",
        notes=[
            "Ctrl+Z undoes your last action. Ctrl+Y (or Ctrl+Shift+Z) redoes an action you just undid.",
            "Excel keeps a long undo history in one session, so you can usually step back through many changes.",
            "AutoSave (when a file is stored on OneDrive/SharePoint) saves your changes automatically every few seconds.",
            "Without AutoSave, save manually and often with Ctrl+S - unsaved work is lost if Excel closes unexpectedly.",
            ".xlsx is the standard modern Excel format. .xls is the older format (limited rows/features). .csv stores plain data only - no formulas, no formatting, no multiple sheets.",
        ],
        practice=[
            "Make a change to any cell, undo it with Ctrl+Z, then redo it with Ctrl+Y.",
            "Open File > Save As and look at the list of file type options - find .xlsx and .csv.",
            "If you have OneDrive, check whether AutoSave is toggled on at the top-left of the Excel window.",
        ],
        quiz=[
            dict(q="Which shortcut undoes your last action?", options=["Ctrl+Z", "Ctrl+Y", "Ctrl+X", "Ctrl+U"], answer=0),
            dict(q="Which shortcut redoes an action you just undid?", options=["Ctrl+Y", "Ctrl+Z", "Ctrl+R", "Ctrl+D"], answer=0),
            dict(q="Which file format stores plain data only, no formulas or formatting?", options=[".csv", ".xlsx", ".xls", ".xltx"], answer=0),
            dict(q="Where must a file be stored for AutoSave to work automatically?", options=["OneDrive/SharePoint", "Desktop", "USB Drive", "Downloads folder"], answer=0),
        ],
    ),
    dict(
        id="U1C8",
        num=8,
        title="Essential Keyboard Shortcuts",
        notes=[
            "Ctrl+S = Save. Ctrl+P = Print. Ctrl+N = New workbook.",
            "Ctrl+B = Bold. Ctrl+I = Italic. Ctrl+U = Underline.",
            "Ctrl+1 = Open Format Cells dialog.",
            "Ctrl+Arrow (any direction) = jump to the edge of a data block in that direction.",
            "Ctrl+Shift+Arrow = select from the current cell to the edge of a data block.",
            "Alt+= = AutoSum: instantly inserts a SUM formula for the numbers above or beside the cell.",
            "Ctrl+Home = jump to A1. Ctrl+End = jump to the last used cell.",
        ],
        practice=[
            "On your practice sheet, select a cell and press Ctrl+1 to open Format Cells - look around, then close it.",
            "Type a few numbers in a column, click the cell below them, and press Alt+= to AutoSum them.",
            "Select some text and press Ctrl+B to bold it.",
            "Select a cell inside a block of data and press Ctrl+Shift+Arrow to select to the edge of that block.",
        ],
        quiz=[
            dict(q="Which shortcut opens the Format Cells dialog?", options=["Ctrl+1", "Ctrl+2", "Ctrl+F", "Alt+1"], answer=0),
            dict(q="Which shortcut instantly inserts a SUM formula (AutoSum)?", options=["Alt+=", "Ctrl+=", "Ctrl+Shift+S", "Alt+S"], answer=0),
            dict(q="Which shortcut makes selected text Bold?", options=["Ctrl+B", "Ctrl+I", "Ctrl+U", "Ctrl+H"], answer=0),
            dict(q="Which shortcut selects to the edge of a data block?", options=["Ctrl+Shift+Arrow", "Ctrl+Arrow", "Shift+Arrow", "Alt+Arrow"], answer=0),
        ],
    ),
]

UNITS = [
    dict(num=1, title="Getting Started", chapters=UNIT1_CHAPTERS),
    dict(num=2, title="Formatting & Sheet Management", chapters=[]),
    dict(num=3, title="Formula Foundations", chapters=[]),
    dict(num=4, title="Logical & Text Functions", chapters=[]),
    dict(num=5, title="Conditional Functions & Data Rules", chapters=[]),
    dict(num=6, title="Organizing & Cleaning Data", chapters=[]),
    dict(num=7, title="Lookup & Reference Functions", chapters=[]),
    dict(num=8, title="Tables, Named Ranges & Dynamic Arrays", chapters=[]),
    dict(num=9, title="Charts & Visualization", chapters=[]),
    dict(num=10, title="What-If Analysis & Financial Basics", chapters=[]),
    dict(num=11, title="Pivot Tables & Dashboards", chapters=[]),
    dict(num=12, title="Power Query", chapters=[]),
    dict(num=13, title="Macros & VBA", chapters=[]),
    dict(num=14, title="Capstone", chapters=[]),
]


def all_chapters_flat():
    """Flat, ordered list of every chapter across every unit, in course order."""
    flat = []
    for unit in UNITS:
        for ch in unit["chapters"]:
            flat.append(ch)
    return flat
