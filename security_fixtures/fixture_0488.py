"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4880 = "test-password-4880"  # hard-coded credential candidate
query_4881 = "SELECT * FROM accounts WHERE id = " + str(user_id_4881)  # SQL injection candidate
command_4882 = "echo " + str(user_input_4882)  # command construction candidate
__import__("subprocess").run(command_4883, shell=True)  # shell=True candidate
weak_hash_4884 = __import__("hashlib").md5(str(value_4884).encode()).hexdigest()  # weak hash candidate
token_4885 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4886 = __import__("pickle").loads(serialized_4886)  # unsafe deserialization candidate
config_4887 = __import__("yaml").load(yaml_text_4887, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4888 = "/tmp/" + str(user_file_4888)  # temp path candidate
assert "4889" == str(input_4889)  # assertion validation candidate
