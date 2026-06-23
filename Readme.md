# Matplotlib & Seaborn Visualization

Chart-building practice notebooks part of a structured data science sprint.

## Progress

### Matplotlib & Seaborn:
- [x] Introduction to Data Visualization
- [x] Plotting Charts using Matplotlib
- [x] Bar Charts in Matplotlib
- [x] Pie Charts in Matplotlib
- [ ] Stack Plots in Matplotlib
- [ ] Histograms in Matplotlib
- [ ] Scatter Plots in Matplotlib
- [ ] Subplots in Matplotlib
- [ ] Introduction to Seaborn
- [ ] Basic Plot Types in Seaborn

## Notebooks
- `Intro To Matplotlib.ipynb` — plt.plot(), xlabel/ylabel/title, legend(), grid(), format strings ('ro--'), readable format (color, linestyle, marker, ms, linewidth), plt.show()
- `Bar Charts in Matplotlib.ipynb` — plt.bar(), grouped bars with np.arange+width offset, bar labels with plt.text(), color
- `Pie Charts in Matplotlib.ipynb` — plt.pie(), labels, colors, explode, shadow, startangle, autopct='%1.1f%%', wedgeprops, donut charts

## Assignment: Pie vs Bar Chart Comparison
-`Filename` — assignment.py
Compare mobile OS market share (Android 72%, iOS 27%, Others 1%) 
using both a pie chart and horizontal bar chart.
Observation: Bar chart makes size differences clearer at a glance — 
pie charts struggle when one slice dominates heavily.

## Notes
- Format strings ('ro--') are compact but don't allow size control — use readable format (color, linestyle, marker, ms) when customization needed.
- `plt.barh()` for horizontal bars when labels are long; `plt.bar()` for vertical.
- `np.arange()` + `width` offset = standard pattern for grouped bar charts.
- `plt.xticks()` replaces numeric index labels with real category names.
- `plt.tight_layout()` prevents label overlap — use it whenever subplots or long labels are involved.
- Pie charts: avoid when comparing many slices — use bar charts instead. Use `explode` to highlight, `autopct='%1.1f%%'` for percentages, `startangle` to rotate.