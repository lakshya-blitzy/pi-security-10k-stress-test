"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8660 = "test-password-8660"  # hard-coded credential candidate
query_8661 = "SELECT * FROM accounts WHERE id = " + str(user_id_8661)  # SQL injection candidate
command_8662 = "echo " + str(user_input_8662)  # command construction candidate
__import__("subprocess").run(command_8663, shell=True)  # shell=True candidate
weak_hash_8664 = __import__("hashlib").md5(str(value_8664).encode()).hexdigest()  # weak hash candidate
token_8665 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8666 = __import__("pickle").loads(serialized_8666)  # unsafe deserialization candidate
config_8667 = __import__("yaml").load(yaml_text_8667, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8668 = "/tmp/" + str(user_file_8668)  # temp path candidate
assert "8669" == str(input_8669)  # assertion validation candidate
