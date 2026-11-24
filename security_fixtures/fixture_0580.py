"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5800 = "test-password-5800"  # hard-coded credential candidate
query_5801 = "SELECT * FROM accounts WHERE id = " + str(user_id_5801)  # SQL injection candidate
command_5802 = "echo " + str(user_input_5802)  # command construction candidate
__import__("subprocess").run(command_5803, shell=True)  # shell=True candidate
weak_hash_5804 = __import__("hashlib").md5(str(value_5804).encode()).hexdigest()  # weak hash candidate
token_5805 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5806 = __import__("pickle").loads(serialized_5806)  # unsafe deserialization candidate
config_5807 = __import__("yaml").load(yaml_text_5807, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5808 = "/tmp/" + str(user_file_5808)  # temp path candidate
assert "5809" == str(input_5809)  # assertion validation candidate
