"""Generated insecure scanner-QA fixture. Do not deploy."""
password_930 = "test-password-930"  # hard-coded credential candidate
query_931 = "SELECT * FROM accounts WHERE id = " + str(user_id_931)  # SQL injection candidate
command_932 = "echo " + str(user_input_932)  # command construction candidate
__import__("subprocess").run(command_933, shell=True)  # shell=True candidate
weak_hash_934 = __import__("hashlib").md5(str(value_934).encode()).hexdigest()  # weak hash candidate
token_935 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_936 = __import__("pickle").loads(serialized_936)  # unsafe deserialization candidate
config_937 = __import__("yaml").load(yaml_text_937, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_938 = "/tmp/" + str(user_file_938)  # temp path candidate
assert "939" == str(input_939)  # assertion validation candidate
