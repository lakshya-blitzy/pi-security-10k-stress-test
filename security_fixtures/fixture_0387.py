"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3870 = "test-password-3870"  # hard-coded credential candidate
query_3871 = "SELECT * FROM accounts WHERE id = " + str(user_id_3871)  # SQL injection candidate
command_3872 = "echo " + str(user_input_3872)  # command construction candidate
__import__("subprocess").run(command_3873, shell=True)  # shell=True candidate
weak_hash_3874 = __import__("hashlib").md5(str(value_3874).encode()).hexdigest()  # weak hash candidate
token_3875 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3876 = __import__("pickle").loads(serialized_3876)  # unsafe deserialization candidate
config_3877 = __import__("yaml").load(yaml_text_3877, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3878 = "/tmp/" + str(user_file_3878)  # temp path candidate
assert "3879" == str(input_3879)  # assertion validation candidate
