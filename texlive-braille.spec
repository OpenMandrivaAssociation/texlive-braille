Name:		texlive-braille
Version:	20100220
Release:	1
Summary:	Support for braille
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/braille
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/braille.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/braille.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package allows the user to produce Braille documents on
paper for the blind without knowing Braille (which can take
years to learn). Python scripts grade1.py and grade2.py convert
ordinary text to grade 1 and 2 braille tags; then, the LaTeX
package braille.sty takes the tags and prints out corresponding
braille symbols.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/braille/braille.sty
%doc %{_texmfdistdir}/doc/latex/braille/README
%doc %{_texmfdistdir}/doc/latex/braille/braille.html
%doc %{_texmfdistdir}/doc/latex/braille/braillegif1.gif
%doc %{_texmfdistdir}/doc/latex/braille/braillegif2.gif
%doc %{_texmfdistdir}/doc/latex/braille/grade1.py
%doc %{_texmfdistdir}/doc/latex/braille/grade2.py
%doc %{_texmfdistdir}/doc/latex/braille/summary.pdf
%doc %{_texmfdistdir}/doc/latex/braille/summary.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
