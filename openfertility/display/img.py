import matplotlib.pyplot as plt
import numpy as np


def show():
    raise NotImplementedError


def grid(
    dataset,
    show_label=True,
    nrows=6,
    ncols=6,
    figsize=(10, 8),
    return_fig=False,
    **kwargs,
):
    """
    Generate a grid of random images from the given dataset.

    Parameters:
        dataset (torch.utils.data.Dataset): The dataset object to visualize as a grid.
        show_label (bool, optional): Whether to show labels for each image. Defaults to True.
        nrows (int, optional): Number of rows in the grid. Defaults to 6.
        ncols (int, optional): Number of columns in the grid. Defaults to 6.
        figsize (tuple, optional): Figure size (width, height) in inches. Defaults to (10, 8).
        return_fig (bool, optional): Whether to return the figure object. Defaults to False.
        **kwargs: Additional keyword arguments to be passed to the underlying `imshow`.

    Returns:
        None or matplotlib.figure.Figure: If `return_fig` is True, returns the matplotlib figure object.
            Otherwise, displays the grid of images and returns None.
    """

    fig, axs = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)

    for axs_row in axs:
        for ax in axs_row:
            idx = np.random.randint(0, len(dataset))
            img = np.transpose(dataset[idx][0], (1, 2, 0))
            ax.imshow(img, **kwargs)
            ax.axis("off")

            if show_label:
                ax.text(
                    0.0,
                    1.0,
                    f" {dataset[idx][1]} ",
                    color="white",
                    fontsize=8,
                    va="top",
                    ha="left",
                    bbox=dict(facecolor="#303030", linewidth=0, pad=0),
                )

    plt.tight_layout(pad=1)

    if return_fig:
        return fig
    else:
        plt.show()
