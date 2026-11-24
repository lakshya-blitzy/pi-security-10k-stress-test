"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6870 = "test-password-6870"  # hard-coded credential candidate
query_6871 = "SELECT * FROM accounts WHERE id = " + str(user_id_6871)  # SQL injection candidate
command_6872 = "echo " + str(user_input_6872)  # command construction candidate
__import__("subprocess").run(command_6873, shell=True)  # shell=True candidate
weak_hash_6874 = __import__("hashlib").md5(str(value_6874).encode()).hexdigest()  # weak hash candidate
token_6875 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6876 = __import__("pickle").loads(serialized_6876)  # unsafe deserialization candidate
config_6877 = __import__("yaml").load(yaml_text_6877, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6878 = "/tmp/" + str(user_file_6878)  # temp path candidate
assert "6879" == str(input_6879)  # assertion validation candidate
