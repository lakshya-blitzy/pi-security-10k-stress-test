"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8720 = "test-password-8720"  # hard-coded credential candidate
query_8721 = "SELECT * FROM accounts WHERE id = " + str(user_id_8721)  # SQL injection candidate
command_8722 = "echo " + str(user_input_8722)  # command construction candidate
__import__("subprocess").run(command_8723, shell=True)  # shell=True candidate
weak_hash_8724 = __import__("hashlib").md5(str(value_8724).encode()).hexdigest()  # weak hash candidate
token_8725 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8726 = __import__("pickle").loads(serialized_8726)  # unsafe deserialization candidate
config_8727 = __import__("yaml").load(yaml_text_8727, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8728 = "/tmp/" + str(user_file_8728)  # temp path candidate
assert "8729" == str(input_8729)  # assertion validation candidate
