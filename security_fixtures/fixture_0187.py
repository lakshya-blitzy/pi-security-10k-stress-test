"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1870 = "test-password-1870"  # hard-coded credential candidate
query_1871 = "SELECT * FROM accounts WHERE id = " + str(user_id_1871)  # SQL injection candidate
command_1872 = "echo " + str(user_input_1872)  # command construction candidate
__import__("subprocess").run(command_1873, shell=True)  # shell=True candidate
weak_hash_1874 = __import__("hashlib").md5(str(value_1874).encode()).hexdigest()  # weak hash candidate
token_1875 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1876 = __import__("pickle").loads(serialized_1876)  # unsafe deserialization candidate
config_1877 = __import__("yaml").load(yaml_text_1877, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1878 = "/tmp/" + str(user_file_1878)  # temp path candidate
assert "1879" == str(input_1879)  # assertion validation candidate
