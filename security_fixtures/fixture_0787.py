"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7870 = "test-password-7870"  # hard-coded credential candidate
query_7871 = "SELECT * FROM accounts WHERE id = " + str(user_id_7871)  # SQL injection candidate
command_7872 = "echo " + str(user_input_7872)  # command construction candidate
__import__("subprocess").run(command_7873, shell=True)  # shell=True candidate
weak_hash_7874 = __import__("hashlib").md5(str(value_7874).encode()).hexdigest()  # weak hash candidate
token_7875 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7876 = __import__("pickle").loads(serialized_7876)  # unsafe deserialization candidate
config_7877 = __import__("yaml").load(yaml_text_7877, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7878 = "/tmp/" + str(user_file_7878)  # temp path candidate
assert "7879" == str(input_7879)  # assertion validation candidate
