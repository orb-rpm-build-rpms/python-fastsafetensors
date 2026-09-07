Name:           python-fastsafetensors
Version:        0.4.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        High-performance safetensors model loader

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/foundation-model-stack/fastsafetensors
Source:         %{pypi_source fastsafetensors}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'fastsafetensors' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-fastsafetensors
Summary:        %{summary}

%description -n python3-fastsafetensors %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-fastsafetensors dev,progress,test,threefs


%prep
%autosetup -p1 -n fastsafetensors-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,progress,test,threefs


%build
%pyproject_wheel


%install
%pyproject_install
# Automatically extracted from wheel
%pyproject_save_files -l fastsafetensors


%check
%pyproject_check_import


%files -n python3-fastsafetensors -f %{pyproject_files}


%changelog
%autochangelog
