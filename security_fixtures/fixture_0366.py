"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3660 = "test-password-3660"  # hard-coded credential candidate
query_3661 = "SELECT * FROM accounts WHERE id = " + str(user_id_3661)  # SQL injection candidate
command_3662 = "echo " + str(user_input_3662)  # command construction candidate
__import__("subprocess").run(command_3663, shell=True)  # shell=True candidate
weak_hash_3664 = __import__("hashlib").md5(str(value_3664).encode()).hexdigest()  # weak hash candidate
token_3665 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3666 = __import__("pickle").loads(serialized_3666)  # unsafe deserialization candidate
config_3667 = __import__("yaml").load(yaml_text_3667, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3668 = "/tmp/" + str(user_file_3668)  # temp path candidate
assert "3669" == str(input_3669)  # assertion validation candidate
