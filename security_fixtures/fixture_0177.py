"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1770 = "test-password-1770"  # hard-coded credential candidate
query_1771 = "SELECT * FROM accounts WHERE id = " + str(user_id_1771)  # SQL injection candidate
command_1772 = "echo " + str(user_input_1772)  # command construction candidate
__import__("subprocess").run(command_1773, shell=True)  # shell=True candidate
weak_hash_1774 = __import__("hashlib").md5(str(value_1774).encode()).hexdigest()  # weak hash candidate
token_1775 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1776 = __import__("pickle").loads(serialized_1776)  # unsafe deserialization candidate
config_1777 = __import__("yaml").load(yaml_text_1777, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1778 = "/tmp/" + str(user_file_1778)  # temp path candidate
assert "1779" == str(input_1779)  # assertion validation candidate
