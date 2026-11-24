"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1880 = "test-password-1880"  # hard-coded credential candidate
query_1881 = "SELECT * FROM accounts WHERE id = " + str(user_id_1881)  # SQL injection candidate
command_1882 = "echo " + str(user_input_1882)  # command construction candidate
__import__("subprocess").run(command_1883, shell=True)  # shell=True candidate
weak_hash_1884 = __import__("hashlib").md5(str(value_1884).encode()).hexdigest()  # weak hash candidate
token_1885 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1886 = __import__("pickle").loads(serialized_1886)  # unsafe deserialization candidate
config_1887 = __import__("yaml").load(yaml_text_1887, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1888 = "/tmp/" + str(user_file_1888)  # temp path candidate
assert "1889" == str(input_1889)  # assertion validation candidate
