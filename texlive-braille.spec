%global tl_name braille
%global tl_revision 20655

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Support for braille
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/braille
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/braille.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/braille.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows the user to produce Braille documents on paper for
the blind without knowing Braille (which can take years to learn).
Python scripts grade1.py and grade2.py convert ordinary text to grade 1
and 2 Braille tags; then, the LaTeX package takes the tags and prints
out corresponding Braille symbols.

