# CSV bar chart generator

### **Input:** A CSV file with first column containing an unique ID that's used for indexing and file names.

### **Output:** Bar charts in PNG format for each row, filenames *&lt;ID&gt;.png*
    
---

### How to use

1. Install required libraries. Check out [Plotly getting started page.](https://plot.ly/python/getting-started/) Orca is needed for the static image files.

2. Create a CSV file (see example below). It needs to have an ID column (could be easily modified to be something else as well) that's used for the image names.

3. Insert the CSV file location to line 10.

4. Customize the things you want, ie. layout. See plotly documentation for more info.

5. Run & enjoy

#### CSV formatting example:

```
ID,January,February,March
ABCD12345,1000,2000,3000
ABCD12346,1500,2500,3500
ABCD12347,2000,3000,4000
```

---

**Note:** IANAD (*I Am Not A Developer*), so this ~~might be~~ is ugly code, illogical, slow etc. This is meant for inspiration only, *not* for any kind of production use anywhere. Heavily commented for the pleasure of other non-developers.