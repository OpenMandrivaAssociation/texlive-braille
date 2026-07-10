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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows the user to produce Braille documents on paper for
the blind without knowing Braille (which can take years to learn).
Python scripts grade1.py and grade2.py convert ordinary text to grade 1
and 2 Braille tags; then, the LaTeX package takes the tags and prints
out corresponding Braille symbols.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/braille
%dir %{_datadir}/texmf-dist/tex/latex/braille
%doc %{_datadir}/texmf-dist/doc/latex/braille/README
%doc %{_datadir}/texmf-dist/doc/latex/braille/braille.html
%doc %{_datadir}/texmf-dist/doc/latex/braille/braillegif1.gif
%doc %{_datadir}/texmf-dist/doc/latex/braille/braillegif2.gif
%doc %{_datadir}/texmf-dist/doc/latex/braille/grade1.py
%doc %{_datadir}/texmf-dist/doc/latex/braille/grade2.py
%doc %{_datadir}/texmf-dist/doc/latex/braille/summary.pdf
%doc %{_datadir}/texmf-dist/doc/latex/braille/summary.tex
%{_datadir}/texmf-dist/tex/latex/braille/braille.sty
