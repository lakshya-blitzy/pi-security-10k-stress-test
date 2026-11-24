"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1920 = "test-password-1920"  # hard-coded credential candidate
query_1921 = "SELECT * FROM accounts WHERE id = " + str(user_id_1921)  # SQL injection candidate
command_1922 = "echo " + str(user_input_1922)  # command construction candidate
__import__("subprocess").run(command_1923, shell=True)  # shell=True candidate
weak_hash_1924 = __import__("hashlib").md5(str(value_1924).encode()).hexdigest()  # weak hash candidate
token_1925 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1926 = __import__("pickle").loads(serialized_1926)  # unsafe deserialization candidate
config_1927 = __import__("yaml").load(yaml_text_1927, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1928 = "/tmp/" + str(user_file_1928)  # temp path candidate
assert "1929" == str(input_1929)  # assertion validation candidate
