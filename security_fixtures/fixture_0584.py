"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5840 = "test-password-5840"  # hard-coded credential candidate
query_5841 = "SELECT * FROM accounts WHERE id = " + str(user_id_5841)  # SQL injection candidate
command_5842 = "echo " + str(user_input_5842)  # command construction candidate
__import__("subprocess").run(command_5843, shell=True)  # shell=True candidate
weak_hash_5844 = __import__("hashlib").md5(str(value_5844).encode()).hexdigest()  # weak hash candidate
token_5845 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5846 = __import__("pickle").loads(serialized_5846)  # unsafe deserialization candidate
config_5847 = __import__("yaml").load(yaml_text_5847, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5848 = "/tmp/" + str(user_file_5848)  # temp path candidate
assert "5849" == str(input_5849)  # assertion validation candidate
