
# coding: utf-8

# ## 1. Introduction
# <p>Everyone loves Lego (unless you ever stepped on one). Did you know by the way that "Lego" was derived from the Danish phrase leg godt, which means "play well"? Unless you speak Danish, probably not. </p>
# <p>In this project, we will analyze a fascinating dataset on every single lego block that has ever been built!</p>
# <p><img src="https://s3.amazonaws.com/assets.datacamp.com/production/project_10/datasets/lego-bricks.jpeg" alt="lego"></p>

# In[68]:


# Nothing to do here


# In[69]:


get_ipython().run_cell_magic('nose', '', 'def test_default():\n  assert True')


# ## 2. Reading Data
# <p>A comprehensive database of lego blocks is provided by <a href="https://rebrickable.com/downloads/">Rebrickable</a>. The data is available as csv files and the schema is shown below.</p>
# <p><img src="https://s3.amazonaws.com/assets.datacamp.com/production/project_10/datasets/downloads_schema.png" alt="schema"></p>
# <p>Let us start by reading in the colors data to get a sense of the diversity of lego sets!</p>

# In[70]:


# Import modules
import pandas as pd

# Read colors data
colors = pd.read_csv('datasets/colors.csv')

# Print the first few rows
colors.head()


# In[71]:


get_ipython().run_cell_magic('nose', '', 'def test_colors_exists():\n    assert \'colors\' in globals(), "You should read the data into a variable named `colors`"')


# ## 3. Exploring Colors
# <p>Now that we have read the <code>colors</code> data, we can start exploring it! Let us start by understanding the number of colors available.</p>

# In[72]:


colors.shape


# In[73]:


num_colors = colors['name'].count()


# In[74]:


print(num_colors)


# In[75]:


get_ipython().run_cell_magic('nose', '', 'def test_num_colors():\n    assert num_colors == 135, "The variable num_colors should equal 135"')


# ## 4. Transparent Colors in Lego Sets
# <p>The <code>colors</code> data has a column named <code>is_trans</code> that indicates whether a color is transparent or not. It would be interesting to explore the distribution of transparent vs. non-transparent colors.</p>

# In[76]:


colors_summary = colors.groupby('is_trans').count()
print(colors_summary)


# In[77]:


get_ipython().run_cell_magic('nose', '', 'def test_colors_summary_exists():\n    assert \'colors_summary\' in globals(), "You should have defined a variable named `colors_summary`"\ndef test_colors_summary():\n    assert colors_summary.shape == (2, 3), "The DataFrame colors_summary should contain 2 rows and 3 columns"')


# ## 5. Explore Lego Sets
# <p>Another interesting dataset available in this database is the <code>sets</code> data. It contains a comprehensive list of sets over the years and the number of parts that each of these sets contained. </p>
# <p><img src="https://imgur.com/1k4PoXs.png" alt="sets_data"></p>
# <p>Let us use this data to explore how the average number of parts in Lego sets has varied over the years.</p>

# In[78]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

# Read sets data as `sets`
sets = pd.read_csv('datasets/sets.csv')

# Create a summary of average number of parts by year: `parts_by_year`
parts_by_year = sets.groupby('year')['num_parts'].mean()


# In[79]:


# Plot trends in average number of parts by year
_ = plt.plot(parts_by_year, marker='+', linestyle='none')


# In[80]:


get_ipython().run_cell_magic('nose', '', 'def test_sets_exists():\n    assert \'sets\' in globals(), "You should read the data into a variable named `sets`"\ndef test_parts_by_year_exists():\n    assert \'parts_by_year\' in globals(), "You should have defined a variable named `parts_by_year`"')


# ## 6. Lego Themes Over Years
# <p>Lego blocks ship under multiple <a href="https://shop.lego.com/en-US/Themes">themes</a>. Let us try to get a sense of how the number of themes shipped has varied over the years.</p>

# In[81]:


themes_by_year = sets.groupby('year')['theme_id'].agg('count').to_frame().reset_index()


# In[82]:


themes_by_year


# In[83]:


get_ipython().run_cell_magic('nose', '', 'def test_themes_by_year_exists():\n    assert \'themes_by_year\' in globals(), "You should have defined a variable named `themes_by_year`"\ndef test_themes_by_year():\n    assert themes_by_year.shape == (66, 2), "The DataFrame themes_by_year should contain 66 rows and 2 columns"\ndef test_themes_by_year_names():\n    colnames = [\'year\', \'theme_id\']\n    assert all(name in themes_by_year for name in colnames), "Your DataFrame, bnames, should have columns named: year, theme_id"')


# ## 7. Wrapping It All Up!
# <p>Lego blocks offer an unlimited amount of fun across ages. We explored some interesting trends around colors, parts, and themes. </p>

# In[84]:


# Nothing to do here


# In[85]:


get_ipython().run_cell_magic('nose', '', 'def test_default():\n  assert True')

