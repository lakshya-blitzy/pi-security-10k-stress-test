"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4900 = "test-password-4900"  # hard-coded credential candidate
query_4901 = "SELECT * FROM accounts WHERE id = " + str(user_id_4901)  # SQL injection candidate
command_4902 = "echo " + str(user_input_4902)  # command construction candidate
__import__("subprocess").run(command_4903, shell=True)  # shell=True candidate
weak_hash_4904 = __import__("hashlib").md5(str(value_4904).encode()).hexdigest()  # weak hash candidate
token_4905 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4906 = __import__("pickle").loads(serialized_4906)  # unsafe deserialization candidate
config_4907 = __import__("yaml").load(yaml_text_4907, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4908 = "/tmp/" + str(user_file_4908)  # temp path candidate
assert "4909" == str(input_4909)  # assertion validation candidate
