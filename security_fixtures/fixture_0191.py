"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1910 = "test-password-1910"  # hard-coded credential candidate
query_1911 = "SELECT * FROM accounts WHERE id = " + str(user_id_1911)  # SQL injection candidate
command_1912 = "echo " + str(user_input_1912)  # command construction candidate
__import__("subprocess").run(command_1913, shell=True)  # shell=True candidate
weak_hash_1914 = __import__("hashlib").md5(str(value_1914).encode()).hexdigest()  # weak hash candidate
token_1915 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1916 = __import__("pickle").loads(serialized_1916)  # unsafe deserialization candidate
config_1917 = __import__("yaml").load(yaml_text_1917, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1918 = "/tmp/" + str(user_file_1918)  # temp path candidate
assert "1919" == str(input_1919)  # assertion validation candidate
