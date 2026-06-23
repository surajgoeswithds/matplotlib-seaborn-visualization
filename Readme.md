# Matplotlib & Seaborn Visualization

Chart-building practice notebooks part of a structured data science sprint.

## Progress

### Matplotlib & Seaborn:
- [x] Introduction to Data Visualization
- [x] Plotting Charts using Matplotlib
- [x] Bar Charts in Matplotlib
- [ ] Pie Charts in Matplotlib
- [ ] Stack Plots in Matplotlib
- [ ] Histograms in Matplotlib
- [ ] Scatter Plots in Matplotlib
- [ ] Subplots in Matplotlib
- [ ] Introduction to Seaborn
- [ ] Basic Plot Types in Seaborn

## Notebooks
- `Intro To Matplotlib.ipynb` — plt.plot(), xlabel/ylabel/title, legend(), grid(), format strings ('ro--'), readable format (color, linestyle, marker, ms, linewidth), plt.show()
- `Bar Charts in Matplotlib.ipynb` — plt.bar(), grouped bars with np.arange+width offset, bar labels with plt.text(), color

## Notes
- Format strings ('ro--') are compact but don't allow size control — use readable format (color, linestyle, marker, ms) when customization needed.
- `plt.barh()` for horizontal bars when labels are long; `plt.bar()` for vertical.
- `np.arange()` + `width` offset = standard pattern for grouped bar charts.
- `plt.xticks()` replaces numeric index labels with real category names.
- `plt.tight_layout()` prevents label overlap — use it whenever subplots or long labels are involved.