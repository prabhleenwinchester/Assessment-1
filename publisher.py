{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0f10c31e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import paho.mqtt.publish as publish\n",
    "publish.single(\"ifn649\", \"Hello World\", hostname=\"ip-addres\")\n",
    "print(\"Done\""
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
