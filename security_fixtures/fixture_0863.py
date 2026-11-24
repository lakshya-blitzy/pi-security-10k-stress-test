"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8630 = "test-password-8630"  # hard-coded credential candidate
query_8631 = "SELECT * FROM accounts WHERE id = " + str(user_id_8631)  # SQL injection candidate
command_8632 = "echo " + str(user_input_8632)  # command construction candidate
__import__("subprocess").run(command_8633, shell=True)  # shell=True candidate
weak_hash_8634 = __import__("hashlib").md5(str(value_8634).encode()).hexdigest()  # weak hash candidate
token_8635 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8636 = __import__("pickle").loads(serialized_8636)  # unsafe deserialization candidate
config_8637 = __import__("yaml").load(yaml_text_8637, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8638 = "/tmp/" + str(user_file_8638)  # temp path candidate
assert "8639" == str(input_8639)  # assertion validation candidate
