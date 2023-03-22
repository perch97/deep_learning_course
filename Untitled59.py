#!/usr/bin/env python
# coding: utf-8

# In[14]:


#import all necessary modules
import numpy as np
import matplotlib.pyplot as plt

from IPython import display
display.set_matplotlib_formats('svg')


# In[ ]:





# In[15]:


#the function

x = np.linspace(-2*np.pi,2*np.pi,401)
fx = np.sin(x)*np.exp(-x**2*.05)

#its derivative
df = np.cos(x)*np.exp(-x**2*.05)+np.sin(x)*(-.1*x)*np.exp(-x**2*.05)

plt.plot(x,fx,x,df)
plt.legend(['f(x)','df'])


# In[16]:


def fx(x):
    return np.sin(x)*np.exp(-x**2*.05)

def deriv(x):
    return np.cos(x)*np.exp(-x**2*.05)-np.sin(x)*.1*x*np.exp(-x**2*.05)


# In[25]:


#random starting point
localmin = np.random.choice(x,1)

#learning parameters

learning_rate = .01
training_epochs = 1000

#run through training
for i in range(training_epochs):
    grad = deriv(localmin)
    localmin = localmin - learning_rate*grad

#plot the results
plt.plot(x,fx(x),x,deriv(x),'--')
plt.plot(localmin,deriv(localmin),'ro')
plt.plot(localmin,fx(localmin),'ro')
plt.xlim(x[[0,-1]])
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(['f(x)','df','f(x) min'])


# # Run parametric experiments

# In[36]:


#Experiment 1: systematically varying the starting locations

startlocs = np.linspace(-5,5,50)
finalres = np.zeros(len(startlocs))

#loop over starting points

for idx,localmin in enumerate(startlocs):
    
    #run through training
    for i in range (training_epochs):
        grad = deriv(localmin)
        localmin = localmin - learning_rate*grad
    #store the final guess
    finalres[idx]=localmin
#plot the results
plt.plot(startlocs,finalres,'s-')
plt.xlabel('Starting guess')
plt.ylabel('final guess')
plt.show()


# In[37]:


# Experiment 2: systematically varying the learning rate

learningrates = np.linspace(1e-10,1e-1,50)
finalres = np.zeros(len(learningrates))

#loop over learning rates
for idx,learningRate in enumerate(learningrates):
    #force starting guess to 0
    localmin = 0
    
    #run through training
    for i in range(training_epochs):
        grad = deriv(localmin)
        localmin=localmin - learningRate*grad
        
    #store the final guess
    finalres[idx] = localmin
    
plt.plot(learningrates,finalres,'s-')
plt.xlabel('Learning rate')
plt.ylabel('Final guess')
plt.show()
    


# In[38]:


#experiment 3: interaction between learning rate and training epochs

#setup parameters
learningrates = np.linspace(1e-10,1e-1,50)
training_epochs = np.round(np.linspace(10,500,40))

#initialize matrix to store results
finalres = np.zeros((len(learningrates),len(training_epochs)))

#loop over learning rates
for Lidx,learningRate in enumerate(learningrates):
    #loop over training epochs
    for Eidx,trainEpochs in enumerate(training_epochs):
        #run through training( again fixing starting location)
        localmin=0
        for i in range(int(trainEpochs)):
            grad=deriv(localmin)
            localmin=localmin-learningRate*grad
            
        #store the final guess
        finalres[Lidx,Eidx] = localmin


# In[42]:


#plot

fig,ax = plt.subplots(figsize=(7,5))

plt.imshow(finalres,extent=[learningrates[0],learningrates[-1],training_epochs[0],training_epochs[-1]],
          aspect = 'auto',origin = 'lower', vmin = -1.45,vmax=-1.2)
plt.xlabel('Learning rate')
plt.ylabel('Training epochs')
plt.title('Final guess')
plt.colorbar()
plt.show()

#another visualization

plt.plot(learningrates,finalres)
plt.xlabel('Learning rates')
plt.ylabel('Final function estimate')
plt.title('Each line is a training epochs N')
plt.show()


# In[ ]:




