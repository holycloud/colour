Colorimetry
===========

Spectral Data Structure
-----------------------

``colour``

.. currentmodule:: colour

.. autosummary::
    :toctree: generated/

    SpectralPowerDistribution
    MultiSpectralPowerDistribution
    SpectralShape
    DEFAULT_SPECTRAL_SHAPE
    ASTME30815_PRACTISE_SHAPE

Spectral Data Generation
------------------------

``colour``

.. currentmodule:: colour

.. autosummary::
    :toctree: generated/

    blackbody_spd
    CIE_standard_illuminant_A_function
    D_illuminant_relative_spd
    constant_spd
    ones_spd
    zeros_spd

``colour.colorimetry``

.. currentmodule:: colour.colorimetry

.. autosummary::
    :toctree: generated/

    blackbody_spectral_radiance
    planck_law

Conversion to Tristimulus Values
--------------------------------

``colour``

.. currentmodule:: colour

.. autosummary::
    :toctree: generated/

    spectral_to_XYZ
    SPECTRAL_TO_XYZ_METHODS
    wavelength_to_XYZ

``colour.colorimetry``

.. currentmodule:: colour.colorimetry

.. autosummary::
    :toctree: generated/

    spectral_to_XYZ_integration
    spectral_to_XYZ_ASTME30815

**Ancillary Objects**

``colour.colorimetry``

.. currentmodule:: colour.colorimetry

.. autosummary::
    :toctree: generated/

    spectral_to_XYZ_tristimulus_weighting_factors_ASTME30815
    adjust_tristimulus_weighting_factors_ASTME30815
    lagrange_coefficients_ASTME202211
    tristimulus_weighting_factors_ASTME202211

Spectral Bandpass Dependence Correction
---------------------------------------

``colour``

.. currentmodule:: colour

.. autosummary::
    :toctree: generated/

    bandpass_correction
    BANDPASS_CORRECTION_METHODS

``colour.colorimetry``

.. currentmodule:: colour.colorimetry

.. autosummary::
    :toctree: generated/

    bandpass_correction_Stearns1988

Colour Matching Functions
-------------------------

``colour.colorimetry``

.. currentmodule:: colour.colorimetry

.. autosummary::
    :toctree: generated/

    LMS_ConeFundamentals
    RGB_ColourMatchingFunctions
    XYZ_ColourMatchingFunctions

**Dataset**

``colour``

.. currentmodule:: colour

.. autosummary::
    :toctree: generated/

    CMFS
    LMS_CMFS
    RGB_CMFS
    STANDARD_OBSERVERS_CMFS

Colour Matching Functions Transformations
-----------------------------------------
**Ancillary Objects**

``colour.colorimetry``

.. currentmodule:: colour.colorimetry

.. autosummary::
    :toctree: generated/

    RGB_2_degree_cmfs_to_XYZ_2_degree_cmfs
    RGB_10_degree_cmfs_to_XYZ_10_degree_cmfs
    RGB_10_degree_cmfs_to_LMS_10_degree_cmfs
    LMS_2_degree_cmfs_to_XYZ_2_degree_cmfs
    LMS_10_degree_cmfs_to_XYZ_10_degree_cmfs

Illuminants and Light Sources
-----------------------------

**Dataset**

``colour``

.. currentmodule:: colour

.. autosummary::
    :toctree: generated/

    ILLUMINANTS
    ILLUMINANTS_RELATIVE_SPDS
    HUNTERLAB_ILLUMINANTS
    LIGHT_SOURCES
    LIGHT_SOURCES_RELATIVE_SPDS

Dominant Wavelength and Purity
------------------------------

``colour``

.. currentmodule:: colour

.. autosummary::
    :toctree: generated/

    dominant_wavelength
    complementary_wavelength
    excitation_purity
    colorimetric_purity

Luminous Efficiency Functions
-----------------------------

``colour``

.. currentmodule:: colour

.. autosummary::
    :toctree: generated/

    luminous_efficacy
    luminous_efficiency
    luminous_flux
    mesopic_luminous_efficiency_function

**Dataset**

.. autosummary::
    :toctree: generated/

    LEFS
    PHOTOPIC_LEFS
    SCOTOPIC_LEFS

Lightness Computation
---------------------

``colour``

.. currentmodule:: colour

.. autosummary::
    :toctree: generated/

    lightness
    LIGHTNESS_METHODS

``colour.colorimetry``

.. currentmodule:: colour.colorimetry

.. autosummary::
    :toctree: generated/

    lightness_CIE1976
    lightness_Fairchild2010
    lightness_Fairchild2011
    lightness_Glasser1958
    lightness_Wyszecki1963

Luminance Computation
---------------------

``colour``

.. currentmodule:: colour

.. autosummary::
    :toctree: generated/

    luminance
    LUMINANCE_METHODS

``colour.colorimetry``

.. currentmodule:: colour.colorimetry

.. autosummary::
    :toctree: generated/

    luminance_ASTMD153508
    luminance_CIE1976
    luminance_Fairchild2010
    luminance_Fairchild2011
    luminance_Newhall1943

Whiteness Computation
---------------------

``colour``

.. currentmodule:: colour

.. autosummary::
    :toctree: generated/

    whiteness
    WHITENESS_METHODS

``colour.colorimetry``

.. currentmodule:: colour.colorimetry

.. autosummary::
    :toctree: generated/

    whiteness_ASTME313
    whiteness_Berger1959
    whiteness_CIE2004
    whiteness_Ganz1979
    whiteness_Stensby1968
    whiteness_Taube1960

Yellowness Computation
----------------------

``colour``

.. currentmodule:: colour

.. autosummary::
    :toctree: generated/

    yellowness
    YELLOWNESS_METHODS

``colour.colorimetry``

.. currentmodule:: colour.colorimetry

.. autosummary::
    :toctree: generated/

    yellowness_ASTMD1925
    yellowness_ASTME313
