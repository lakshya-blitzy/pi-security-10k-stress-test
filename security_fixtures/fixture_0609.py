"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6090 = "test-password-6090"  # hard-coded credential candidate
query_6091 = "SELECT * FROM accounts WHERE id = " + str(user_id_6091)  # SQL injection candidate
command_6092 = "echo " + str(user_input_6092)  # command construction candidate
__import__("subprocess").run(command_6093, shell=True)  # shell=True candidate
weak_hash_6094 = __import__("hashlib").md5(str(value_6094).encode()).hexdigest()  # weak hash candidate
token_6095 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6096 = __import__("pickle").loads(serialized_6096)  # unsafe deserialization candidate
config_6097 = __import__("yaml").load(yaml_text_6097, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6098 = "/tmp/" + str(user_file_6098)  # temp path candidate
assert "6099" == str(input_6099)  # assertion validation candidate
