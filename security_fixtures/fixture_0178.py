"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1780 = "test-password-1780"  # hard-coded credential candidate
query_1781 = "SELECT * FROM accounts WHERE id = " + str(user_id_1781)  # SQL injection candidate
command_1782 = "echo " + str(user_input_1782)  # command construction candidate
__import__("subprocess").run(command_1783, shell=True)  # shell=True candidate
weak_hash_1784 = __import__("hashlib").md5(str(value_1784).encode()).hexdigest()  # weak hash candidate
token_1785 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1786 = __import__("pickle").loads(serialized_1786)  # unsafe deserialization candidate
config_1787 = __import__("yaml").load(yaml_text_1787, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1788 = "/tmp/" + str(user_file_1788)  # temp path candidate
assert "1789" == str(input_1789)  # assertion validation candidate
