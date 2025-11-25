/*
 * This file contains all the functions required to modify the ni-webcharts cartesian graphs based on TestStand's data-layout and data-orientation attributes
 * A thing to note is that a lot of the functions have multiple ways to set the 'value' attribute, which modifes the graph.
 * The reason for that is Chrome & Vivaldi and pretty much any Node related browser/server allow setting attributes using the [] operators.
 * IE, FF and Edge do not.
 * IE also does not support e6 (ECMAScript6) standards, so we cannot use for-of constructs which would make the code more readable as a lot of it deals with manipulating arrays 
 */

// modify array values implementation
function modifyImpl(element) {
    var dataLayout = element.getAttribute("DataLayout");

    if (dataLayout != null) {
        if (dataLayout.length != 0) {
            var dataOrientation = element.getAttribute("DataOrientation");

            if (dataOrientation != null) {
                dataOrientation = dataOrientation.toLowerCase();
                if (dataOrientation.length != 0) {
                    // Now we can go ahead and modify the array values of the graph.
                    switch (dataLayout.toLowerCase()) {
                        case "MultipleY".toLowerCase():
                            if (dataOrientation == "Row Based".toLowerCase()) {
                                myRow(element);
                            }
                            else if (dataOrientation == "Column Based".toLowerCase()) {
                                myColumn(element);
                            }
                            break;
                        case "SingleX-MultipleY".toLowerCase():
                            if (dataOrientation == "Row Based".toLowerCase()) {
                                sxmyRow(element);
                            }
                            else if (dataOrientation == "Column Based".toLowerCase()) {
                                sxmyColumn(element);
                            }
                            break;
                        default:
                            // Don't do anything
                            break;
                    }
                }
            }
        }
    }
}

function myRow(element) {
    // We don't have to do anything as the data is already in the format we want it to be in.
}

function myColumn(element) {
    // A basic transpose of the array values is required here
    try {
        var initialArrayValues = JSON.parse(element.getAttribute("value"));
        initialArrayValues = transposeArray(initialArrayValues)
        element.setAttribute("value", initialArrayValues);
        element["value"] = initialArrayValues;
        // The new e6 format is not supported on multiple browsers (I'm looking at you, IE11)
        // element["value"] = initialArrayValues[0].map((col, i) => initialArrayValues.map(row => row[i]));
    } catch (err) {
        // Swallow all exceptions.
        console.log(err.message);
    }
}

function sxmyRow(element) {
    // From the TestStand 2017 help documentation:
    // Multiple XY plots. A plot is created for each row in the array.
    // The X coordinates of the plotted points are the array data values in the first row of the array.
    // The Y coordinates of the plotted points are the array data values of every row in the array except the first row.

    // Example array received from TestStand:
    /* TS repr: []
    Locals.Array2D[0][0] = 3
    Locals.Array2D[1][0] = 5
    Locals.Array2D[2][0] = 7
    Locals.Array2D[0][1] = 2
    Locals.Array2D[1][1] = 9
    Locals.Array2D[2][1] = 6
    Locals.Array2D[0][2] = 1
    Locals.Array2D[1][2] = 8
    Locals.Array2D[2][2] = 0
    
    element value repr:
    [[3.000000, 2.000000, 1.000000], [5.000000, 9.000000, 8.000000], [7.000000, 6.000000, 0.000000]]
    
    Desired output: [
        [{x: 3, y: 5}, {x: 2, y: 9}, {x: 1, y: 8}],
        [{x: 3, y: 7}, {x: 2, y: 6}, {x: 1, y: 0}]
    ]
    
    X-indices: row indices (3, 2, 1)
    Y-indices: column indices EXCEPT row 1 (5, 7), (9, 6), (8, 0)
    */

    try {
        var initialArrayValues = JSON.parse(element.getAttribute("value"));
        var ycord = sxmyCommon(initialArrayValues);
        element.setAttribute("value", ycord);
        element["value"] = ycord;
    } catch (err) {
        // Swallow all exceptions.
        console.log(err.message);
    }
}

function sxmyColumn(element) {
    // From the TestStand 2017 help documentation:
    // Multiple XY plots. A plot is created for each column in the array.
    // The X coordinates of the plotted points are the array data values in the first column of the array
    // The Y coordinates of the plotted points are the array data values of every column in the array except the first column.

    try {
        var initialArrayValues = JSON.parse(element.getAttribute("value"));
        initialArrayValues = transposeArray(initialArrayValues);
        var ycord = sxmyCommon(initialArrayValues);
        element.setAttribute("value", ycord);
        element["value"] = ycord;
    } catch (err) {
        // Swallow all exceptions.
        console.log(err.message);
    }
}

function sxmyCommon(initialArrayValues) {
    var rows = initialArrayValues.length;
    var columns = initialArrayValues[0].length;

    // X coordinates: [x1, x2, x3], [y1, y2, y3], [y1', y2', y3']
    var xcord = initialArrayValues[0];
    
    // Y coordinates (the y's) : [x1, x2, x3], [y1, y2, y3], [y1', y2', y3']
    var ycord = [];
    var tempArray = [];
    var tempObj = {};
    for (var rowitr = 1; rowitr < rows; ++rowitr) {
        tempArray = [];
        for (var colitr = 0; colitr < columns; ++colitr) {
            tempObj = {x: xcord[colitr], y: initialArrayValues[rowitr][colitr]};
            tempArray.push(tempObj);
        }
        ycord.push(tempArray.slice(0));
    }

    return ycord;
}

function transposeArray(arrayElement) {
    return arrayElement[0].map(function (_, c) { 
        return arrayElement.map(function (r) { 
            return r[c];
        });
    });
}

// Function which will look at data layout and orientation attributes and modify the graph representation based on that.
function modifyLayoutAndOrientation() {
    // Obtain the list of graphs
    var graphElements = document.querySelectorAll("ni-cartesian-graph");

    // Iterate through the graph elements and update their array values to output the desired layout and orientation
    for (var itr = 0; itr < graphElements.length; ++itr) {
        modifyImpl(graphElements[itr]);
    }
    // graphElements.forEach(function (element) {
    //     modifyImpl(element);
    // });
}

modifyLayoutAndOrientation();
