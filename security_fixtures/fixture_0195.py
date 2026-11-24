"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1950 = "test-password-1950"  # hard-coded credential candidate
query_1951 = "SELECT * FROM accounts WHERE id = " + str(user_id_1951)  # SQL injection candidate
command_1952 = "echo " + str(user_input_1952)  # command construction candidate
__import__("subprocess").run(command_1953, shell=True)  # shell=True candidate
weak_hash_1954 = __import__("hashlib").md5(str(value_1954).encode()).hexdigest()  # weak hash candidate
token_1955 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1956 = __import__("pickle").loads(serialized_1956)  # unsafe deserialization candidate
config_1957 = __import__("yaml").load(yaml_text_1957, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1958 = "/tmp/" + str(user_file_1958)  # temp path candidate
assert "1959" == str(input_1959)  # assertion validation candidate
