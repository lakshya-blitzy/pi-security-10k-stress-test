"""Generated insecure scanner-QA fixture. Do not deploy."""
password_870 = "test-password-870"  # hard-coded credential candidate
query_871 = "SELECT * FROM accounts WHERE id = " + str(user_id_871)  # SQL injection candidate
command_872 = "echo " + str(user_input_872)  # command construction candidate
__import__("subprocess").run(command_873, shell=True)  # shell=True candidate
weak_hash_874 = __import__("hashlib").md5(str(value_874).encode()).hexdigest()  # weak hash candidate
token_875 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_876 = __import__("pickle").loads(serialized_876)  # unsafe deserialization candidate
config_877 = __import__("yaml").load(yaml_text_877, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_878 = "/tmp/" + str(user_file_878)  # temp path candidate
assert "879" == str(input_879)  # assertion validation candidate
